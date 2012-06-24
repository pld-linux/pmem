Summary:	pmem - display memory information about processes
Summary(pl.UTF-8):   pmem - wyświetlanie ilości pamięci zużywanej przez proces
Name:		pmem
Version:	1.1.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.pmem.net/%{name}-%{version}.tar.gz
# Source0-md5:	bfc9e80a6896e24cffb0e83373c22d52
URL:		http://www.pmem.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pmem is a small command line utility for all Linux und Unix operating
systems to display memory information of running processes. To do
this, pmem reads the memory information that are provided by the /proc
file systems. Therefore, pmem does not work on operating systems that
do not maintain this files system.

%description -l pl.UTF-8
pmem jest małym narzędziem dla wszystkich systemów linuksowych i
uniksowych. Wyświetla informacje o pamięci zajmowanej przez
uruchomione procesy. pmem osiąga to przez odczytywanie informacji
zawartych w systemie plików /proc.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/pmem
