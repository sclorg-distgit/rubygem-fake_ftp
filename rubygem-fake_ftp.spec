%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

#Generated from fake_ftp-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fake_ftp

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.1
Release: 3%{?dist}
Summary: Creates a fake FTP server for use in testing
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/fake_ftp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.6
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.6
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Testing FTP? Use this!

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

#remove .files
rm -f .%{gem_instdir}/.gitignore
rm -f .%{gem_instdir}/.rspec
rm -f .%{gem_instdir}/.travis.yml

%install
mkdir -p %{buildroot}%{gem_dir}

cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite

%check
pushd .%{gem_instdir}
#tests require networking capabilities, disabling for now
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Guardfile
%{gem_instdir}/fake_ftp.gemspec
%doc %{gem_instdir}/CONTRIBUTORS.md

%changelog
* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 0.1.1-3
- Add SCL macros

* Tue Feb 17 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-2
- Move CONTRIBUTORS.md to doc subpackage
- Fixed description
- Removed trailing whitespace

* Thu Feb 12 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-1
- Initial package
