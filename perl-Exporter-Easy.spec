#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Easy
Version  : 0.18
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Easy-0.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Easy-0.18.tar.gz
Summary  : 'Takes the drudgery out of Exporting symbols'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Exporter-Easy-license = %{version}-%{release}
Requires: perl-Exporter-Easy-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Exporter-Easy,
version 0.18:
Takes the drudgery out of Exporting symbols

%package dev
Summary: dev components for the perl-Exporter-Easy package.
Group: Development
Provides: perl-Exporter-Easy-devel = %{version}-%{release}
Requires: perl-Exporter-Easy = %{version}-%{release}

%description dev
dev components for the perl-Exporter-Easy package.


%package license
Summary: license components for the perl-Exporter-Easy package.
Group: Default

%description license
license components for the perl-Exporter-Easy package.


%package perl
Summary: perl components for the perl-Exporter-Easy package.
Group: Default
Requires: perl-Exporter-Easy = %{version}-%{release}

%description perl
perl components for the perl-Exporter-Easy package.


%prep
%setup -q -n Exporter-Easy-0.18
cd %{_builddir}/Exporter-Easy-0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Exporter-Easy
cp %{_builddir}/Exporter-Easy-0.18/LICENSE %{buildroot}/usr/share/package-licenses/perl-Exporter-Easy/c4d45ac20684b7598d4f17ac71d259ebe3e10d7d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Exporter::Easiest.3
/usr/share/man/man3/Exporter::Easy.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Exporter-Easy/c4d45ac20684b7598d4f17ac71d259ebe3e10d7d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
