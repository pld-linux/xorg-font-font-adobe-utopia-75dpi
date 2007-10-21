Summary:	Adobe Utopia 75dpi bitmap font
Summary(pl.UTF-8):	Font bitmapowy 75dpi Adobe Utopia
Name:		xorg-font-font-adobe-utopia-75dpi
Version:	1.0.1
Release:	2
License:	distributable (see COPYING)
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-adobe-utopia-75dpi-%{version}.tar.bz2
# Source0-md5:	dd912284e4750023f9682812532fa033
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 0.99.2
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adobe Utopia 75dpi bitmap font.

This package includes Unicode font as well as in ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-9, ISO-8859-10,
ISO-8859-13, ISO-8859-14 and ISO-8859-15 encodings.

%description -l pl.UTF-8
Font bitmapowy 75dpi Adobe Utopia.

Ten pakiet zawiera font unikodowy, a także w kodowaniach ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-9, ISO-8859-10,
ISO-8859-13, ISO-8859-14 i ISO-8859-15.

%prep
%setup -q -n font-adobe-utopia-75dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/75dpi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 75dpi

%postun
fontpostinst 75dpi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/75dpi/UT*.pcf.gz
