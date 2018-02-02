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

%description
%{common_desc}

%package -n python2-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python2-%{service}-tests-tempest}
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
BuildRequires:  openstack-macros

Requires:   python-tempest >= 1:16.0.0
Requires:   python-oslo-config
Requires:   python-oslo-log
Requires:   python-oslo-messaging
Requires:   python-paramiko
Requires:   python-eventlet
Requires:   python-keystoneauth1
Requires:   python-testtools
Requires:   python-cinderclient
Requires:   python-gnocchiclient
Requires:   python-heatclient
Requires:   python-neutronclient
Requires:   python-novaclient
Requires:   python-swiftclient
Requires:   python-zaqarclient
Requires:   python-testscenarios
Requires:   python-gabbi
Requires:   python-kombu

%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:16.0.0
Requires:   python3-oslo-config
Requires:   python3-oslo-log
Requires:   python3-oslo-messaging
Requires:   python3-paramiko
Requires:   python3-eventlet
Requires:   python3-keystoneauth1
Requires:   python3-testtools
Requires:   python3-cinderclient
Requires:   python3-gnocchiclient
Requires:   python3-heatclient
Requires:   python3-neutronclient
Requires:   python3-novaclient
Requires:   python3-swiftclient
Requires:   python3-zaqarclient
Requires:   python3-testscenarios
Requires:   python3-gabbi
Requires:   python3-kombu

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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/heat-tempest-plugin/commit/?id=8257d55634be0d5decf0827c6ddd50831210750f
