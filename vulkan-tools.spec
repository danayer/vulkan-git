%global source_date_epoch_from_changelog 0

Name:           vulkan-tools
Version:        1.4.330
Release:        0.1%{?dist}
Summary:        Vulkan tools

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Tools
Source0:        %url/archive/refs/tags/v%{version}.tar.gz      
Source1:        volk.h

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  glslang
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  vulkan-volk-devel

Provides:       vulkan-demos%{?_isa} = %{version}-%{release}
Obsoletes:      vulkan-demos < %{version}-%{release}

%description
Vulkan tools

%prep
%autosetup -n Vulkan-Tools-%{version}


%build
%cmake3 -GNinja -DCMAKE_BUILD_TYPE=Release -DGLSLANG_INSTALL_DIR=%{_prefix} -DVulkanHeaders_INCLUDE_DIR=%{_includedir}/vulkan
%cmake3_build


%install
%cmake3_install

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*

%changelog
