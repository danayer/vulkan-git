%global source_date_epoch_from_changelog 0
%global __python %{__python3}

Name:           vulkan-headers
Version:        1.4.341
Release:        0.1%{?dist}
Summary:        Vulkan Header files and API registry

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        %url/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake3 gcc gcc-c++ ninja-build
BuildArch:      noarch       

%description
Vulkan Header files and API registry

%prep
%autosetup -n Vulkan-Headers-%{version} -p1


%build
%cmake3 -G Ninja -DCMAKE_INSTALL_LIBDIR=%{_libdir} .
%cmake_build


%install
%cmake_install


%files
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/
%dir %{_datadir}/cmake/VulkanHeaders
%{_datadir}/cmake/VulkanHeaders/*.cmake

%changelog

