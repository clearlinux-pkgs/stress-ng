#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stress-ng
Version  : V0.05.12
Release  : 5
URL      : https://github.com/ColinIanKing/stress-ng/archive/V0.05.12.tar.gz
Source0  : https://github.com/ColinIanKing/stress-ng/archive/V0.05.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: stress-ng-bin
Requires: stress-ng-doc
BuildRequires : keyutils-dev

%description
stress-ng
stress-ng will stress test a computer system in various selectable ways. It
was designed to exercise various physical subsystems of a computer as well as
the various operating system kernel interfaces. Stress-ng features:

%package bin
Summary: bin components for the stress-ng package.
Group: Binaries

%description bin
bin components for the stress-ng package.


%package doc
Summary: doc components for the stress-ng package.
Group: Documentation

%description doc
doc components for the stress-ng package.


%prep
%setup -q -n stress-ng-0.05.12

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stress-ng

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
