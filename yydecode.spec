Summary(pl):	Narzêdzie do dekodowania plikow w formacie yEnc
Name:		yydecode
Version:	0.2.7
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://prdownloads.sourceforge.net/yydecode/yydecode-0.2.7.tar.gz
URL:		http://yydecode.sourceforge.net/
Packager:	Arkadiusz 'Jo Joro' Sochala
BuildRequires:  autoconf
BuildRequires:  automake
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
yydecode is a decoder for yEnc encoded binaries as recently found on Usenet.
yydecode works almost identi cally to the infamous uudecode program.

%prep
%setup  -q 

%build
%configure -q
  
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

			
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install {TODO,README,ChangeLog,NEWS,AUTHORS,COPYING} $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}
%{_mandir}/man1/*.gz
%doc /usr/share/doc/%{name}-%{version}
