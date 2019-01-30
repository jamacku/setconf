Name:           setconf
Version:        0.7.5 
Release:        1%{?dist}
Summary:        Small utility that can be used for changing settings in configuration text files. 

License:        GPLv2
URL:            http://setconf.roboticoverlords.org/ 
Source0:        https://github.com/xyproto/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildArch:      noarch

%description
Setconf is small utility that can be used for changing settings in configuration text files. It has no dependencies except the built-in Python modules. 

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n %{name}
%license COPYING
%doc README.md
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/%{name}.*.py*
%{_bindir}/%{name}

%changelog
* Tue Jan 29 2019 Jan Macku <jamacku@redhat.com> - 0.7.5-1 
- First setconf package  
