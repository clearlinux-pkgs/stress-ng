#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stress-ng
Version  : 0.08.07
Release  : 10
URL      : https://github.com/ColinIanKing/stress-ng/archive/V0.08.07.tar.gz
Source0  : https://github.com/ColinIanKing/stress-ng/archive/V0.08.07.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: stress-ng-bin
Requires: stress-ng-doc
Requires: stress-ng-data
BuildRequires : keyutils-dev

%description
stress-ng
stress-ng will stress test a computer system in various selectable ways. It
was designed to exercise various physical subsystems of a computer as well as
the various operating system kernel interfaces. Stress-ng features:

%package bin
Summary: bin components for the stress-ng package.
Group: Binaries
Requires: stress-ng-data

%description bin
bin components for the stress-ng package.


%package data
Summary: data components for the stress-ng package.
Group: Data

%description data
data components for the stress-ng package.


%package doc
Summary: doc components for the stress-ng package.
Group: Documentation

%description doc
doc components for the stress-ng package.


%prep
%setup -q -n stress-ng-0.08.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1498699339
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1498699339
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
