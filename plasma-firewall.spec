#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-firewall
Version  : 6.3.1
Release  : 20
URL      : https://download.kde.org/stable/plasma/6.3.1/plasma-firewall-6.3.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.1/plasma-firewall-6.3.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.1/plasma-firewall-6.3.1.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 FSFAP GPL-2.0 GPL-3.0 LGPL-3.0
Requires: plasma-firewall-data = %{version}-%{release}
Requires: plasma-firewall-lib = %{version}-%{release}
Requires: plasma-firewall-license = %{version}-%{release}
Requires: plasma-firewall-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : python3-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Plasma 5 Firewall KCM
This is the repository for the Plasma 5 Firewall KCM.
# Requirements
Plasma 5 Firewall has few dependencies mainly from Qt5 and KF5 with minimum required version being
- Qt                              >= 5.10.0
- KDE Workspace         >= 5.8.0
- Plasma Framework    >= 5.32

%package data
Summary: data components for the plasma-firewall package.
Group: Data

%description data
data components for the plasma-firewall package.


%package dev
Summary: dev components for the plasma-firewall package.
Group: Development
Requires: plasma-firewall-lib = %{version}-%{release}
Requires: plasma-firewall-data = %{version}-%{release}
Provides: plasma-firewall-devel = %{version}-%{release}
Requires: plasma-firewall = %{version}-%{release}

%description dev
dev components for the plasma-firewall package.


%package lib
Summary: lib components for the plasma-firewall package.
Group: Libraries
Requires: plasma-firewall-data = %{version}-%{release}
Requires: plasma-firewall-license = %{version}-%{release}

%description lib
lib components for the plasma-firewall package.


%package license
Summary: license components for the plasma-firewall package.
Group: Default

%description license
license components for the plasma-firewall package.


%package locales
Summary: locales components for the plasma-firewall package.
Group: Default

%description locales
locales components for the plasma-firewall package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n plasma-firewall-6.3.1
cd %{_builddir}/plasma-firewall-6.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739916124
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739916124
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-firewall
cp %{_builddir}/plasma-firewall-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/plasma-firewall/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/FSFAP.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/e91dcdf6eb4e675db1aee8b8fb8394bdfcb22d49 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-firewall-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-firewall/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_firewall

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kde_ufw_plugin_helper.py
/usr/lib64/libexec/kf6/kauth/kde_ufw_plugin_helper

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_firewall.desktop
/usr/share/dbus-1/system-services/org.kde.ufw.service
/usr/share/dbus-1/system.d/org.kde.ufw.conf
/usr/share/kcm_ufw/defaults
/usr/share/metainfo/org.kde.plasma.firewall.metainfo.xml
/usr/share/polkit-1/actions/org.kde.ufw.policy

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkcm_firewall_core.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/kf6/plasma_firewall/firewalldbackend.so
/usr/lib64/qt6/plugins/kf6/plasma_firewall/ufwbackend.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_firewall.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-firewall/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-firewall/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-firewall/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/plasma-firewall/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-firewall/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/plasma-firewall/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-firewall/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/plasma-firewall/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/plasma-firewall/e91dcdf6eb4e675db1aee8b8fb8394bdfcb22d49

%files locales -f kcm_firewall.lang
%defattr(-,root,root,-)

