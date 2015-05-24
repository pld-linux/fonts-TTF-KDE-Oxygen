Summary:	Oxygen fonts created by the KDE Community
Name:		fonts-TTF-KDE-Oxygen
Version:	5.3.0
Release:	1
License:	OFL or GPLv3 with exceptions
Group:		Fonts
Source0:	http://download.kde.org/stable/plasma/%{version}/oxygen-fonts-%{version}.tar.xz
# Source0-md5:	1899f95757694bf849ff0661797e09d2
Source1:	61-oxygen-sans.conf
Source2:	61-oxygen-mono.conf
URL:		http://www.kde.org/
BuildRequires:	cmake
BuildRequires:	fontforge
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Oxygen fonts created by the KDE Community.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q -n oxygen-fonts-%{version}

%build
install -d build
cd build
%{cmake} \
	-DOXYGEN_FONT_INSTALL_DIR=%{_ttffontsdir} \
	..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_sysconfdir}/fonts/conf.d,%{_datadir}/fontconfig/conf.avail}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/61-oxygen-sans.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/61-oxygen-mono.conf

ln -s %{_datadir}/fontconfig/conf.avail/61-oxygen-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/61-oxygen-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_ttffontsdir}/Oxygen*.ttf
%{_datadir}/fontconfig/conf.avail/61-oxygen-*.conf
%{_sysconfdir}/fonts/conf.d/61-oxygen-*.conf

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/OxygenFont

