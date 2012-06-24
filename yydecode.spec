Summary:	Decoder for yEnc-encoded binaries
Summary(pl):	Narz�dzie do dekodowania plik�w w formacie yEnc
Name:		yydecode
Version:	0.2.7
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://prdownloads.sourceforge.net/yydecode/%{name}-%{version}.tar.gz
URL:		http://yydecode.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yydecode is a decoder for yEnc encoded binaries as recently found on
Usenet. yydecode works almost identically to the infamous uudecode
program.

%description -l pl
yydecode to dekoder do plik�w zakodowanych przez yEnc, kt�re mo�na
znale�� w usenecie. Dzia�a prawie identycznie jak znany uudecode.

%prep
%setup -q

%build
%configure -q

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf TODO README ChangeLog NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {TODO,README,ChangeLog,NEWS,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
