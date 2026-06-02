Name:     tofi
Version:  0.9.1
Release:  %autorelease
Summary:  Tiny dynamic menu for Wayland
License:  MIT
Url:      https://github.com/philj56/tofi
Source:   https://github.com/philj56/tofi/archive/refs/tags/v%{version}.tar.gz#$/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(scdoc)

%description
An extremely fast and simple dmenu/rofi replacement for wlroots-based Wayland
compositors such as Sway.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/tofi
%{_bindir}/tofi-drun
%{_bindir}/tofi-run
%dir %{_sysconfdir}/xdg/tofi
%config %{_sysconfdir}/xdg/tofi/config
%{_mandir}/man1/tofi*
%{_mandir}/man5/tofi.5*

%files bash-completion
%{_datadir}/bash-completion/*

%changelog
%autochangelog