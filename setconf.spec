Name:           setconf
Version:        0.7.5 
Release:        1%{?dist}
Summary:        Utility for changing settings in configuration text files 

License:        GPLv2
URL:            http://setconf.roboticoverlords.org/ 
Source0:        https://github.com/xyproto/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         %{name}-%{version}-rm_sb.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildArch:      noarch

%description
Setconf is small utility that can be used for
changing settings in configuration text files. 

%prep
%autosetup -n %{name}-%{version}
ls
mkdir -p %{buildroot}%{_mandir}/man1/
ls -R %{buildroot}
install -m0644 -p %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
ls -R %{buildroot}

%build
%py3_build

%check
%{__python3} setconf.py --test
awk '/^..\/setconf.py/ { print "%{__python3} " $0; next } { print }' testcases/test.sh >testcases/test.sh
./testcases/test.sh

%install
%py3_install

%files
%license COPYING
%doc README.md
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/%{name}.*.pyc
%{_mandir}/man1/%{name}.1
%{_bindir}/%{name}

%changelog
* Wed Feb 6 2019 Jan Macku <jamacku@redhat.com> - 0.7.5-1 
- Init setconf package  
