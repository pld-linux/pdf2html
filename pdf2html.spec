Summary:	PDF to HTML converter
Summary(pl):	Konwerter plików PDF do HTML-a
Name:		pdf2html
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/%{name}/%{name}-%{version}.tgz
Patch0:		%{name}-pld.patch
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/pdf2html/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libpng-devel
Requires:	ghostscript

%description
PDF to HTML converter.

%description -l pl
Konwerter PDF do HTML.

%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/var/lib/pdf2html

install pbm2eps9	$RPM_BUILD_ROOT%{_bindir}
install pbm2png		$RPM_BUILD_ROOT%{_bindir}
install pdf2html	$RPM_BUILD_ROOT%{_bindir}
install ps2eps9		$RPM_BUILD_ROOT%{_bindir}
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
/var/lib/%{name}
