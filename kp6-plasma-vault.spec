#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.3.5
%define		qtver		5.15.2
%define		kpname		plasma-vault

Summary:	KDE Plasma Vault
Name:		kp6-%{kpname}
Version:	6.3.5
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	d46012b7d1b6f54130327f0253621169
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	fontconfig-devel
BuildRequires:	kf6-attica-devel
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kcmutils-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kdeclarative-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	kf6-kglobalaccel-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-knewstuff-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-knotifyconfig-devel
BuildRequires:	kf6-kpeople-devel
BuildRequires:	kf6-krunner-devel
BuildRequires:	kf6-kwallet-devel
BuildRequires:	kp6-libplasma-devel >= %{version}
BuildRequires:	kp6-plasma-activities-stats-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Plasma Vault is an open-source encryption solution for KDE with which
you can create encrypted folders to contain private files of any
format.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/plasmavault.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/plasmavaultfileitemaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.vault.so
%{_datadir}/metainfo/org.kde.plasma.vault.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.vault
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents/ui/VaultItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/metadata.json
