%global service heat
%global plugin heat-tempest-plugin
%global module heat_tempest_plugin

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora}
%global with_python3 1
%endif

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

%package -n python2-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python2-%{service}-tests-tempest}
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

Obsoletes:   python-heat-tests < 10.0.0

Requires:   python2-tempest >= 1:17.2.0
Requires:   python2-oslo-config >= 2:4.0.0
Requires:   python2-oslo-log >= 3.30.0
Requires:   python2-oslo-messaging >= 5.29.0
Requires:   python2-paramiko >= 2.0.0
Requires:   python2-eventlet
Requires:   python2-keystoneauth1 >= 3.3.0
Requires:   python2-testtools >= 1.8.0
Requires:   python2-cinderclient >= 3.3.0
Requires:   python2-gnocchiclient >= 3.3.1
Requires:   python2-heatclient >= 1.10.0
Requires:   python2-neutronclient >= 6.3.0
Requires:   python2-novaclient >= 9.1.0
Requires:   python2-swiftclient >= 3.2.0
Requires:   python2-zaqarclient >= 1.0.0
Requires:   python2-testscenarios >= 0.4
Requires:   python2-gabbi >= 1.33.0
Requires:   python2-kombu
Requires:   python2-os-client-config >= 1.28.0

%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:17.2.0
Requires:   python3-oslo-config >= 2:4.0.0
Requires:   python3-oslo-log >= 3.30.0
Requires:   python3-oslo-messaging >= 5.29.0
Requires:   python3-paramiko >= 2.0.0
Requires:   python3-eventlet
Requires:   python3-keystoneauth1 >= 3.3.0
Requires:   python3-testtools >= 1.8.0
Requires:   python3-cinderclient >= 3.3.0
Requires:   python3-gnocchiclient >= 3.3.1
Requires:   python3-heatclient >= 1.10.0
Requires:   python3-neutronclient >= 6.3.0
Requires:   python3-novaclient >= 9.1.0
Requires:   python3-swiftclient >= 3.2.0
Requires:   python3-zaqarclient >= 1.0.0
Requires:   python3-testscenarios >= 0.4
Requires:   python3-gabbi >= 1.33.0
Requires:   python3-kombu
Requires:   python3-os-client-config >= 1.28.0

%description -n python3-%{service}-tests-tempest
%{common_desc}
%endif

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{module}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info
%endif

%changelog

