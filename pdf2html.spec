Summary:	PDF to HTML converter
Summary(pl):	Konwerter plik�w PDF do HTML-a
Name:		pdf2html
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/%{name}/%{name}-%{version}.tgz
# Source0-md5:	974a675c5158dd03ba21bab0971d106d
Patch0:		%{name}-pld.patch
Patch1:		%{name}-gcc3.patch
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/pdf2html/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libpng-devel
Requires:	ghostscript

%description
PDF to HTML converter.

%description -l pl
Konwerter PDF do HTML-a.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc CHANGELOG README
/var/lib/%{name}
