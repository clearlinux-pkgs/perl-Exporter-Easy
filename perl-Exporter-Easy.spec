#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Easy
Version  : 0.18
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Easy-0.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Easy-0.18.tar.gz
Summary  : 'Takes the drudgery out of Exporting symbols'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Exporter-Easy-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Exporter-Easy,
version 0.18:
Takes the drudgery out of Exporting symbols

%package dev
Summary: dev components for the perl-Exporter-Easy package.
Group: Development
Provides: perl-Exporter-Easy-devel = %{version}-%{release}

%description dev
dev components for the perl-Exporter-Easy package.


%package license
Summary: license components for the perl-Exporter-Easy package.
Group: Default

%description license
license components for the perl-Exporter-Easy package.


%prep
%setup -q -n Exporter-Easy-0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Exporter-Easy
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Exporter-Easy/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Easiest.pm
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Easy.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Exporter::Easiest.3
/usr/share/man/man3/Exporter::Easy.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Exporter-Easy/LICENSE
