#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stress-ng
Version  : 0.09.52
Release  : 33
URL      : https://github.com/ColinIanKing/stress-ng/archive/V0.09.52.tar.gz
Source0  : https://github.com/ColinIanKing/stress-ng/archive/V0.09.52.tar.gz
Summary  : stress-ng will stress test a computer system in various selectable ways
Group    : Development/Tools
License  : GPL-2.0
Requires: stress-ng-bin = %{version}-%{release}
Requires: stress-ng-data = %{version}-%{release}
Requires: stress-ng-license = %{version}-%{release}
Requires: stress-ng-man = %{version}-%{release}
BuildRequires : keyutils-dev

%description
stress-ng
stress-ng will stress test a computer system in various selectable ways. It
was designed to exercise various physical subsystems of a computer as well as
the various operating system kernel interfaces. Stress-ng features:

%package bin
Summary: bin components for the stress-ng package.
Group: Binaries
Requires: stress-ng-data = %{version}-%{release}
Requires: stress-ng-license = %{version}-%{release}
Requires: stress-ng-man = %{version}-%{release}

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
%setup -q -n stress-ng-0.09.52

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549510921
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1549510921
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stress-ng
cp COPYING %{buildroot}/usr/share/package-licenses/stress-ng/COPYING
cp debian/copyright %{buildroot}/usr/share/package-licenses/stress-ng/debian_copyright
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stress-ng

%files data
%defattr(-,root,root,-)
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
/usr/share/package-licenses/stress-ng/COPYING
/usr/share/package-licenses/stress-ng/debian_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/stress-ng.1.gz
