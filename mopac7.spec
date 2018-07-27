Summary:	A library for semi-empirical QM calculations
Summary(pl.UTF-8):	Biblioteka do semiempirycznych obliczeń z zakresu mechaniki kwantowej
Name:		mopac7
Version:	1.15
Release:	5
License:	Public Domain
Group:		Libraries
Source0:	http://bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
# Source0-md5:	7e509fd03154b37cc682593365c233f4
Patch0:		%{name}-paths.patch
URL:		http://sourceforge.net/projects/mopac7/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gcc-fortran
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for semi-empirical QM calculations.

%description -l pl.UTF-8
Biblioteka do semiempirycznych obliczeń z zakresu mechaniki kwantowej.

%package devel
Summary:	Header files for MOPAC7 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MOPAC7
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MOPAC7 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MOPAC7.

%package static
Summary:	Static MOPAC7 library
Summary(pl.UTF-8):	Statyczna biblioteka MOPAC7
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MOPAC7 library.

%description static -l pl.UTF-8
Statyczna biblioteka MOPAC7.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmopac7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmopac7.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmopac7.so
%{_libdir}/libmopac7.la
%{_includedir}/mopac7
%{_pkgconfigdir}/libmopac7.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmopac7.a
