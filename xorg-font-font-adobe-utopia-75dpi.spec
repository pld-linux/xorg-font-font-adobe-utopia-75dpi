Summary:	adobe-utopia-75dpi font
Summary(pl):	Font adobe-utopia-75dpi
Name:		xorg-font-font-adobe-utopia-75dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-adobe-utopia-75dpi-%{version}.tar.bz2
# Source0-md5:	c7084294f3038a5d26ffbafc2651864d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
adobe-utopia-75dpi font.

%description -l pl
Font adobe-utopia-75dpi.

%prep
%setup -q -n font-adobe-utopia-75dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
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
%{_libdir}/X11/fonts/75dpi/*
