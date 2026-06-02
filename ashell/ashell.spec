%define debug_package %{nil}

Name:           ashell
Summary:        A ready-to-go Wayland status bar for Hyprland and Niri
Version:        0.8.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/MalpenZibo/ashell

# Tell Copr that the file is sitting right next to the spec inside the directory
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc-c++
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  dbus-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  pipewire-devel

%description
A beautiful, responsive, ready-to-use Wayland status bar built specifically 
for the Hyprland and Niri compositors using the iced GUI toolkit.

%prep
# Ensure this matches the exact folder name hidden inside your custom tarball
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
install -D -p -m 0755 target/release/ashell %{buildroot}%{_bindir}/ashell

%files
%license LICENSE
%{_bindir}/ashell

%changelog
* Tue Jun 02 2026 Maintainer <artzx@fedora.org> - 0.8.0-1
- Localized tarball and spec layou