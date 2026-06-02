%define debug_package %{nil}

Name:           ashell
Summary:        A ready-to-go Wayland status bar for Hyprland and Niri
Version:        0.8.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/MalpenZibo/ashell
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

# Essential toolchains for building the Rust ecosystem
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc-c++

# Native system libraries required by iced/wgpu graphics backends
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  dbus-devel
BuildRequires:  vulkan-loader-devel

%description
A beautiful, responsive, ready-to-use Wayland status bar built specifically 
for the Hyprland and Niri compositors using the iced GUI toolkit.

%prep
%autosetup

%build
# Tell cargo to compile the production optimized binary
cargo build --release

%install
# Create the target destination directory and copy ONLY the compiled binary asset
install -D -p -m 0755 target/release/ashell %{buildroot}%{_bindir}/ashell

%files
%license LICENSE
%{_bindir}/ashell

%changelog
* Tue Jun 02 2026 Maintainer <artzx@fedora.org> - 0.8.0-1
- Initial pristine functional package build