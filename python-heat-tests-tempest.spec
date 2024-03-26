%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318
%global service heat
%global plugin heat-tempest-plugin
%global module heat_tempest_plugin

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests to cover the Heat project. \
Additionally it provides a plugin to automatically load these \
tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    2.1.0
Release:    1%{?dist}
Summary:    Tempest Integration of Heat Project
License:    Apache-2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{plugin}-%{upstream_version} -S git

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.dist-info

%changelog
* Tue Mar 26 2024 RDO <dev@lists.rdoproject.org> 2.1.0-1
- Update to 2.1.0

