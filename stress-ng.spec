#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stress-ng
Version  : 0.14.05
Release  : 122
URL      : https://github.com/ColinIanKing/stress-ng/archive/V0.14.05/stress-ng-0.14.05.tar.gz
Source0  : https://github.com/ColinIanKing/stress-ng/archive/V0.14.05/stress-ng-0.14.05.tar.gz
Summary  : stress-ng will stress test a computer system in various selectable ways
Group    : Development/Tools
License  : GPL-2.0
Requires: stress-ng-bin = %{version}-%{release}
Requires: stress-ng-data = %{version}-%{release}
Requires: stress-ng-license = %{version}-%{release}
Requires: stress-ng-man = %{version}-%{release}
Requires: intel-ipsec-mb
BuildRequires : intel-ipsec-mb-dev
BuildRequires : keyutils-dev

%description
# stress-ng (stress next generation)
stress-ng will stress test a computer system in various selectable ways. It
was designed to exercise various physical subsystems of a computer as well as
the various operating system kernel interfaces. Stress-ng features:

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
%setup -q -n stress-ng-0.14.05
cd %{_builddir}/stress-ng-0.14.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663178036
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1663178036
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stress-ng
cp %{_builddir}/stress-ng-%{version}/COPYING %{buildroot}/usr/share/package-licenses/stress-ng/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
