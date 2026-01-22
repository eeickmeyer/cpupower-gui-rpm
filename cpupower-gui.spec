Name:           cpupower-gui
Version:        1.0.0
Release:        1%{?dist}
Summary:        GUI utility to change the CPU frequency

%global debug_package %{nil}

License:        GPL-3.0-or-later
URL:            https://github.com/vagnum08/cpupower-gui
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        cpupower-gui.1
Patch0:         97f8ac02.patch

BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.50.0
BuildRequires:  ninja-build
BuildRequires:  pkgconf
BuildRequires:  python3
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros

Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-xdg
Requires:       /usr/bin/gapplication

%description
cpupower-gui is a graphical (GUI) utility to change the CPU frequency.
This utility can change the operating frequency of the CPU for each core
separately. Additionally, the cpu governor can be changed.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/cpupower-gui.1

%post
%systemd_post cpupower-gui.service
%systemd_user_post cpupower-gui-user.service

%preun
%systemd_preun cpupower-gui.service
%systemd_user_preun cpupower-gui-user.service

%postun
%systemd_postun cpupower-gui.service
%systemd_user_postun cpupower-gui-user.service
:

%files

%license COPYING
%doc README.md
%dir %{_datadir}/cpupower-gui
%dir %{_libdir}/cpupower-gui
%dir %{_sysconfdir}/cpupower_gui.d
%{_bindir}/cpupower-gui
%{_mandir}/man1/cpupower-gui.1*
%{_datadir}/applications/org.rnd2.cpupower_gui.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.rnd2.cpupower_gui.svg
%{_datadir}/cpupower-gui/cpupower-gui.gresource
%{_datadir}/cpupower-gui/scaling-governors.conf
%{_datadir}/cpupower-gui/cpupower_gui/__init__.py
%{_datadir}/cpupower-gui/cpupower_gui/config.py
%{_datadir}/cpupower-gui/cpupower_gui/helper.py
%{_datadir}/cpupower-gui/cpupower_gui/main.py
%{_datadir}/cpupower-gui/cpupower_gui/utils.py
%{_datadir}/cpupower-gui/cpupower_gui/window.py
%{_datadir}/metainfo/org.rnd2.cpupower_gui.appdata.xml

# Config files
%config(noreplace) %{_sysconfdir}/cpupower_gui.conf
%config(noreplace) %{_sysconfdir}/cpupower_gui.d/README
%config(noreplace) %{_sysconfdir}/cpupower_gui.d/my_profile.profile.ex

# Systemd services
%{_unitdir}/cpupower-gui-helper.service
%{_unitdir}/cpupower-gui.service
%{_userunitdir}/cpupower-gui-user.service

# Helper binary
%{_libdir}/cpupower-gui/cpupower-gui-helper

# D-Bus services
%{_datadir}/dbus-1/services/org.rnd2.cpupower_gui.service
%{_datadir}/dbus-1/system-services/org.rnd2.cpupower_gui.helper.service
%{_datadir}/dbus-1/system.d/org.rnd2.cpupower_gui.helper.conf

# GSettings schema
%{_datadir}/glib-2.0/schemas/org.rnd2.cpupower_gui.gschema.xml

# Locales
%lang(el_GR) %{_datadir}/locale/el_GR/LC_MESSAGES/cpupower-gui.mo
%lang(en) %{_datadir}/locale/en/LC_MESSAGES/cpupower-gui.mo
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/cpupower-gui.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/cpupower-gui.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/cpupower-gui.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/cpupower-gui.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/cpupower-gui.mo

# Polkit
%{_datadir}/polkit-1/actions/org.rnd2.cpupower-gui.policy
%{_datadir}/polkit-1/rules.d/org.rnd2.cpupower-gui.rules

%changelog
* Fri Jan 16 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.0.0-1
- Initial Fedora RPM release

