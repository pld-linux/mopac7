Summary:	A library for semi-empirical QM calculations
Summary(pl):	Biblioteka do semiempirycznych oblicze� z zakresu mechaniki kwantowej
Name:		mopac7
Version:	1.11
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://dl.sourceforge.net/mopac7/%{name}-%{version}.tar.gz
# Source0-md5:	501c34ad4995d127dca8461a05ceb66a
URL:		http://sourceforge.net/projects/mopac7/
# requires libg2c or libf2c
BuildRequires:	gcc-g77 < 5:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for semi-empirical QM calculations.

%description -l pl
Biblioteka do semiempirycznych oblicze� z zakresu mechaniki kwantowej.

%package devel
Summary:	Header files for MOPAC7 library
Summary(pl):	Pliki nag��wkowe biblioteki MOPAC7
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# just libg2c-devel or libf2c-devel
Requires:	gcc-g77 < 5:3.0

%description devel
Header files for MOPAC7 library.

%description devel -l pl
Pliki nag��wkowe biblioteki MOPAC7.

%package static
Summary:	Static MOPAC7 library
Summary(pl):	Statyczna biblioteka MOPAC7
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MOPAC7 library.

%description static -l pl
Statyczna biblioteka MOPAC7.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmopac7.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmopac7.so
%{_libdir}/libmopac7.la
%{_includedir}/mopac7
%{_pkgconfigdir}/libmopac7.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmopac7.a
