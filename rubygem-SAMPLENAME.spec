%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name SAMPLENAME

%define rubyabi 1.9.1

Summary:    Summary
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.1
Release:    1%{?dist}
Group:      Development/Libraries
License:    GPLv2
URL:        https://SAMPLENAME.com
Source0:    http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   %{?scl_prefix}ruby(abi) >= %{rubyabi}
Requires:   %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Description for SAMPLENAME

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T -n %{gem_name}-%{version}

%build
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{gem_dir}
%{gem_spec}

%files doc
%defattr(-,root,root,-)

%changelog
* Sat May 25 2013 John Matthews <jwmatthews@gmail.com> 0.0.1-1
- Initial commit

