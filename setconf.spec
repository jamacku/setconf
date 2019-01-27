Name:           setconf
Version:        0.7.5 
Release:        1%{?dist}
Summary:        Small utility that can be used for changing settings in configuration textfiles. 

License:        GPLv2
URL:            http://setconf.roboticoverlords.org/ 
Source0:        http://setconf.roboticoverlords.org/%{name}-%{version}.tar.xz

BuildRequires:  python3-devel

BuildArch:      noarch

%description
Setconf is small utility that can be used for changing settings in configuration textfiles. It has no dependencies except the built-in Python modules. 

%prep
%autosetup

%build
%py3_build
python setup.py build && python setup.py install
# python -m compileall %{name}.py

%install
%py3_install
rm -rf $RPM_BUILD_ROOT

%files
%license COPYING
%doc README.md
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/
%{_bindir}/%{name}

%changelog
* Tue Jan 22 2019 Jan Macku <jamacku@redhat.com> - 0.7.5-1 
- First setconf package  
