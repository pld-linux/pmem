Summary:	pmem - display memory information about processes
Summary(pl):	pmem - wy¶wietlanie ilo¶ci pamiêci zu¿ywanej przez proces
Name:		pmem
Version:	1.1.1
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.pmem.net/%{name}-%{version}.tar.gz
# Source0-md5:	ce08243475be7d94af5c3f5c330b95e4
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

%description -l pl
pmem jest ma³ym narzêdziem dla wszystkich systemów linuksowych i
uniksowych. Wy¶wietla informacje o pamiêci zajmowanej przez
uruchomione procesy. pmem osi±ga to przez odczytywanie informacji
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
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/pmem
