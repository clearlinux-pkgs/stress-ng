#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v10
# autospec commit: 5905be9
#
Name     : stress-ng
Version  : 0.17.08
Release  : 166
URL      : https://github.com/ColinIanKing/stress-ng/archive/V0.17.08/stress-ng-0.17.08.tar.gz
Source0  : https://github.com/ColinIanKing/stress-ng/archive/V0.17.08/stress-ng-0.17.08.tar.gz
Summary  : stress-ng will stress test a computer system in various selectable ways
Group    : Development/Tools
License  : GPL-2.0
Requires: stress-ng-bin = %{version}-%{release}
Requires: stress-ng-data = %{version}-%{release}
Requires: stress-ng-license = %{version}-%{release}
Requires: stress-ng-man = %{version}-%{release}
Requires: gmp
Requires: intel-ipsec-mb
Requires: mpfr
BuildRequires : Judy-dev
BuildRequires : attr-dev
BuildRequires : eigen-dev
BuildRequires : gmp-dev
BuildRequires : intel-ipsec-mb-dev
BuildRequires : keyutils-dev
BuildRequires : kmod-dev
BuildRequires : libaio-dev
BuildRequires : libbsd-dev
BuildRequires : libcap-dev
BuildRequires : libgcrypt-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : mesa-dev
BuildRequires : mpfr-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# stress-ng (stress next generation)
<a href="https://repology.org/project/stress-ng/versions">
<img src="https://repology.org/badge/vertical-allrepos/stress-ng.svg" alt="Packaging status" align="right">
</a>

%package bin
Summary: bin components for the stress-ng package.
Group: Binaries
Requires: stress-ng-data = %{version}-%{release}
Requires: stress-ng-license = %{version}-%{release}

%description bin
bin components for the stress-ng package.


%package data
Summary: data components for the stress-ng package.
Group: Data

%description data
data components for the stress-ng package.


%package license
Summary: license components for the stress-ng package.
Group: Default

%description license
license components for the stress-ng package.


%package man
Summary: man components for the stress-ng package.
Group: Default

%description man
man components for the stress-ng package.


%prep
%setup -q -n stress-ng-0.17.08
cd %{_builddir}/stress-ng-0.17.08
pushd ..
cp -a stress-ng-0.17.08 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714642324
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
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
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
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
export SOURCE_DATE_EPOCH=1714642324
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stress-ng
cp %{_builddir}/stress-ng-%{version}/COPYING %{buildroot}/usr/share/package-licenses/stress-ng/4cc77b90af91e615a64ae04893fdffa7939db84c || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/stress-ng
/usr/bin/stress-ng

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/stress-ng
/usr/share/stress-ng/example-jobs/cpu-cache.job
/usr/share/stress-ng/example-jobs/cpu.job
/usr/share/stress-ng/example-jobs/device.job
/usr/share/stress-ng/example-jobs/example.job
/usr/share/stress-ng/example-jobs/filesystem.job
/usr/share/stress-ng/example-jobs/hot-cpu.job
/usr/share/stress-ng/example-jobs/interrupt.job
/usr/share/stress-ng/example-jobs/io.job
/usr/share/stress-ng/example-jobs/matrix-methods.job
/usr/share/stress-ng/example-jobs/memory.job
/usr/share/stress-ng/example-jobs/network.job
/usr/share/stress-ng/example-jobs/pipe.job
/usr/share/stress-ng/example-jobs/scheduler.job
/usr/share/stress-ng/example-jobs/security.job
/usr/share/stress-ng/example-jobs/vm.job

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stress-ng/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/stress-ng.1.gz
