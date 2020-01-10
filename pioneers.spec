Summary: 	Playable implementation of the Settlers of Catan 
Name: 		pioneers
Version: 	15.1
Release:        2
Group: 		Games/Boards
License: 	GPLv2+
Url: 		http://pio.sourceforge.net/
Source: 	http://downloads.sourceforge.net/project/pio/Source/%{name}-%{version}.tar.gz
Source2:	pioneers-0.9.55-icons.tar.bz2
Patch: pioneers-0.12.1-desktopentry.patch
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify) >= 0.7.4
BuildRequires:  avahi-client-devel
BuildRequires:  scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
Provides: gnocatan
Obsoletes: gnocatan

%description 
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.

%package 	server-console
Summary:	Pioneers Console Server
Group: 		Games/Boards
Requires:	pioneers-server-data = %version
Provides: gnocatan-server-console
Obsoletes: gnocatan-server-console
%description 	server-console
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.
The meta server registers available game servers and offers them to new
players. It can also create new servers on client request.


%package 	server-gtk
Summary:	Pioneers GTK Server
Group: 		Games/Boards
Requires:	pioneers-server-data = %version
Provides: gnocatan-server-gtk
Obsoletes: gnocatan-server-gtk
%description 	server-gtk
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.

The server has a user interface in which you can customise the game
parameters.  Customisation is fairly limited at the moment, but this
should change in later versions.  Once you are happy with the game
parameters, press the Start Server button, and the server will start
listening for client connections.

%package 	server-data
Summary: 	Pioneers Data
Group: 		Games/Boards
Provides: gnocatan-server-data
Obsoletes: gnocatan-server-data
%description 	server-data
Pioneers is an Internet playable implementation of the Settlers of
Catan board game.  The aim is to remain as faithful to the board game
as is possible.

This package contains the data files for a game server, including a
computer player that can take part in Pioneers games.


%prep
%setup -q -a 2
%autopatch -p1


%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std
%find_lang %name --with-gnome
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Boards" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

cp -r icons %buildroot%_datadir/

%files -f %name.lang
%doc AUTHORS ChangeLog README
%{_bindir}/pioneers
%{_bindir}/pioneers-editor
%{_datadir}/applications/pioneers.desktop
%{_datadir}/applications/pioneers-editor.desktop
%{_datadir}/pixmaps/pioneers.png
%{_datadir}/pixmaps/pioneers-editor.png
%{_datadir}/pixmaps/pioneers/
%dir %{_datadir}/games/pioneers
%{_datadir}/games/pioneers/themes/
%{_mandir}/man6/pioneers.6*
%{_mandir}/man6/pioneers-editor.6*
%if %mdvver <= 201100
%_datadir/omf/pioneers
%endif
%_datadir/icons/hicolor/*/apps/pioneers.*
%_datadir/icons/hicolor/*/apps/pioneers-editor.*
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name-editor.png
%_liconsdir/%name-editor.png
%_miconsdir/%name-editor.png

%files server-console
%doc README
%{_bindir}/pioneers-server-console
%{_bindir}/pioneers-metaserver
%{_mandir}/man6/pioneers-server-console.6*
%{_mandir}/man6/pioneers-metaserver.6*

%files server-gtk
%doc README
%{_bindir}/pioneers-server-gtk
%{_datadir}/applications/pioneers-server.desktop
%{_mandir}/man6/pioneers-server-gtk.6*
%_datadir/pixmaps/%name-server.png
%_datadir/icons/hicolor/*/apps/pioneers-server.*
%_iconsdir/%name-server.png
%_liconsdir/%name-server.png
%_miconsdir/%name-server.png

%files server-data
%doc README
%{_bindir}/pioneersai
%{_mandir}/man6/pioneersai.6*
%dir %{_datadir}/games/pioneers
%{_datadir}/games/pioneers/computer_names
%{_datadir}/games/pioneers/*.game

