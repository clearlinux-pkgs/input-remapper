#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v4
# autospec commit: da8b975a5699
#
Name     : input-remapper
Version  : input.mapper.2.0.0
Release  : 1
URL      : https://github.com/sezanzeb/input-remapper/archive/2.0.0/input-mapper-2.0.0.tar.gz
Source0  : https://github.com/sezanzeb/input-remapper/archive/2.0.0/input-mapper-2.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: input-remapper-bin = %{version}-%{release}
Requires: input-remapper-config = %{version}-%{release}
Requires: input-remapper-data = %{version}-%{release}
Requires: input-remapper-license = %{version}-%{release}
Requires: input-remapper-python = %{version}-%{release}
Requires: input-remapper-python3 = %{version}-%{release}
Requires: input-remapper-services = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(evdev)
BuildRequires : pypi(pydantic)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center"><img src="data/input-remapper.svg" width=100/></p>
<h1 align="center">Input Remapper</h1>

%package bin
Summary: bin components for the input-remapper package.
Group: Binaries
Requires: input-remapper-data = %{version}-%{release}
Requires: input-remapper-config = %{version}-%{release}
Requires: input-remapper-license = %{version}-%{release}
Requires: input-remapper-services = %{version}-%{release}

%description bin
bin components for the input-remapper package.


%package config
Summary: config components for the input-remapper package.
Group: Default

%description config
config components for the input-remapper package.


%package data
Summary: data components for the input-remapper package.
Group: Data

%description data
data components for the input-remapper package.


%package license
Summary: license components for the input-remapper package.
Group: Default

%description license
license components for the input-remapper package.


%package python
Summary: python components for the input-remapper package.
Group: Default
Requires: input-remapper-python3 = %{version}-%{release}

%description python
python components for the input-remapper package.


%package python3
Summary: python3 components for the input-remapper package.
Group: Default
Requires: python3-core
Requires: pypi(evdev)
Requires: pypi(pydantic)
Requires: pypi(setuptools)

%description python3
python3 components for the input-remapper package.


%package services
Summary: services components for the input-remapper package.
Group: Systemd services
Requires: systemd

%description services
services components for the input-remapper package.


%prep
%setup -q -n input-remapper-2.0.0
cd %{_builddir}/input-remapper-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708554971
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
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

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
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/input-remapper
cp %{_builddir}/input-remapper-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/input-remapper/31a3d460bb3c7d98845187c716a30db81c44b615 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/input-remapper-control
/usr/bin/input-remapper-gtk
/usr/bin/input-remapper-reader-service
/usr/bin/input-remapper-service

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/99-input-remapper.rules

%files data
%defattr(-,root,root,-)
/usr/share/applications/input-remapper-gtk.desktop
/usr/share/input-remapper/99-input-remapper.rules
/usr/share/input-remapper/input-remapper-autoload.desktop
/usr/share/input-remapper/input-remapper-gtk.desktop
/usr/share/input-remapper/input-remapper-large.png
/usr/share/input-remapper/input-remapper.glade
/usr/share/input-remapper/input-remapper.policy
/usr/share/input-remapper/input-remapper.service
/usr/share/input-remapper/input-remapper.svg
/usr/share/input-remapper/inputremapper.Control.conf
/usr/share/input-remapper/io.github.sezanzeb.input_remapper.metainfo.xml
/usr/share/input-remapper/lang/fr/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/fr_FR/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/it/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/it_IT/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/ru/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/ru_RU/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/sk/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/sk_SK/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/uk/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/uk_UA/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/zh/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/lang/zh_CN/LC_MESSAGES/input-remapper.mo
/usr/share/input-remapper/style.css
/usr/share/metainfo/io.github.sezanzeb.input_remapper.metainfo.xml
/usr/share/polkit-1/actions/input-remapper.policy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/input-remapper/31a3d460bb3c7d98845187c716a30db81c44b615

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/input-remapper.service
