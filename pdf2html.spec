Summary:	PDF to HTML converter
Summary(pl):	Konwerter plików PDF do HTML-a
Name:		pdf2html
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/%{name}
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/%{name}/%{name}-%{version}.tgz
Patch0:		%{name}-pld.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	libpng
Requires:	zlib
Requires:	ghostscript

%description
PDF to HTML converter

%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/var/lib/pdf2html

install pbm2eps9	$RPM_BUILD_ROOT/%{_bindir}
install pbm2png		$RPM_BUILD_ROOT/%{_bindir}
install pdf2html	$RPM_BUILD_ROOT/%{_bindir}
install ps2eps9		$RPM_BUILD_ROOT/%{_bindir}
install left.png	$RPM_BUILD_ROOT/var/lib/%{name}
install right.png 	$RPM_BUILD_ROOT/var/lib/%{name}
install idx.png		$RPM_BUILD_ROOT/var/lib/%{name}

gzip -9nf CHANGELOG README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
%dir /var/lib/%{name}
/var/lib/%{name}/*
