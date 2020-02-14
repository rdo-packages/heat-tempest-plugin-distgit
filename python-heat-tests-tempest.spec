# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global service heat
%global plugin heat-tempest-plugin
%global module heat_tempest_plugin

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests to cover the Heat project. \
Additionally it provides a plugin to automatically load these \
tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Heat Project
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python%{pyver}-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python%{pyver}-%{service}-tests-tempest}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools

Obsoletes:   python-heat-tests < 1:10.0.0

Requires:   python%{pyver}-tempest >= 1:18.0.0
Requires:   python%{pyver}-oslo-config >= 2:5.2.0
Requires:   python%{pyver}-oslo-log >= 3.36.0
Requires:   python%{pyver}-oslo-messaging >= 5.35.0
Requires:   python%{pyver}-paramiko >= 2.0.0
Requires:   python%{pyver}-eventlet
Requires:   python%{pyver}-keystoneauth1 >= 3.4.0
Requires:   python%{pyver}-testtools >= 1.8.0
Requires:   python%{pyver}-cinderclient >= 3.5.0
Requires:   python%{pyver}-gnocchiclient >= 7.0.1
Requires:   python%{pyver}-heatclient >= 1.14.0
Requires:   python%{pyver}-neutronclient >= 6.7.0
Requires:   python%{pyver}-novaclient >= 10.1.0
Requires:   python%{pyver}-swiftclient >= 3.5.0
Requires:   python%{pyver}-zaqarclient >= 1.9.0
Requires:   python%{pyver}-testscenarios >= 0.5.0
Requires:   python%{pyver}-gabbi >= 1.42.1
Requires:   python%{pyver}-kombu
Requires:   python%{pyver}-os-client-config >= 1.29.0
Requires:   os-collect-config >= 5.0.0
%description -n python%{pyver}-%{service}-tests-tempest
%{common_desc}

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{pyver_build}

%install
%{pyver_install}

%files -n python%{pyver}-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/*.egg-info

%changelog
