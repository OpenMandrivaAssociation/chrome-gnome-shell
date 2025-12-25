%global debug_package %{nil}

Name:		chrome-gnome-shell
Version:	12.1
Release:	1
Summary:	Support for managing GNOME Shell Extensions through web browsers
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
#Source0:	https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
Source0:  https://gitlab.gnome.org/GNOME/gnome-browser-extension/-/archive/v%{version}/gnome-browser-extension-v%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:  gettext
BuildRequires:	pkgconfig(python)
BuildRequires:	coreutils
BuildRequires:	jq
BuildRequires:  7zip

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
%autosetup -n gnome-browser-extension-v%{version} -p1

%build
%meson

%meson_build

%install
%meson_install

%check

%files
%license LICENSE

