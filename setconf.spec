Name:           setconf
Version:        0.7.5 
Release:        1%{?dist}
Summary:        Small utility that can be used for changing settings in configuration textfiles. 

License:        GPLv2
URL:            http://setconf.roboticoverlords.org/ 
Source0:        https://github.com/xyproto/%{name}/archive/%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch:      noarch

%description
Setconf is small utility that can be used for changing settings in configuration textfiles. It has no dependencies except the built-in Python modules. 

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n %{name}
%license COPYING
%doc README.md
%{python3_sitelib}/*
%{_bindir}/%{name}

%changelog
* Tue Jan 22 2019 Jan Macku <jamacku@redhat.com> - 0.7.5-1 
- First setconf package  
