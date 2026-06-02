%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}

Name: ashell
Summary: A ready to go Wayland status bar for Hyprland
Version: 0.8.0
Release: 1%{?dist}
License: MIT
Group: Applications/System
Source0: ashell-{version}.tar.gz
URL: https://github.com/MalpenZibo/ashell

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*