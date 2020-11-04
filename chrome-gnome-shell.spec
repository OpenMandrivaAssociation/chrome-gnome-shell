%global debug_package %{nil}

Name:		chrome-gnome-shell
Version:	10.1
Release:	3
Summary:	Support for managing GNOME Shell Extensions through web browsers
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:	https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	pkgconfig(python)
BuildRequires:	coreutils
BuildRequires:	jq

Requires:	dbus
Requires:	gnome-icon-theme
Requires:	gnome-shell
Requires:	hicolor-icon-theme
#Requires:	mozilla-filesystem
Requires:	python3dist(pygobject)
Requires:	python-requests

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and
other Browser Extension, Chrome Extension or WebExtensions capable browsers)
and native host messaging connector that provides integration with GNOME Shell
and the corresponding extensions repository https://extensions.gnome.org.

%prep
%autosetup

%build
  %cmake -DBUILD_EXTENSION=OFF \
         -DCMAKE_INSTALL_LIBDIR=%{_lib} \
         -DPython_ADDITIONAL_VERSIONS=3 \
         ..
  %make_build

%install
%make_install -C build

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop

%files
%license LICENSE
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/
%{_bindir}/chrome-gnome-shell
%{_libdir}/mozilla/native-messaging-hosts/
%{python3_sitelib}/chrome_gnome_shell-*.egg-info
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_datadir}/icons/gnome/*/apps/org.gnome.ChromeGnomeShell.png

