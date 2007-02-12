Summary:	Decoder for yEnc-encoded binaries
Summary(pl.UTF-8):   Narzędzie do dekodowania plików w formacie yEnc
Name:		yydecode
Version:	0.2.10
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/yydecode/%{name}-%{version}.tar.gz
# Source0-md5:	9e6c5eb009f9084f7cbe7e4b766b12d8
URL:		http://yydecode.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yydecode is a decoder for yEnc encoded binaries as recently found on
Usenet. yydecode works almost identically to the infamous uudecode
program.

%description -l pl.UTF-8
yydecode to dekoder do plików zakodowanych przez yEnc, które można
znaleźć w usenecie. Działa prawie identycznie jak znany uudecode.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
