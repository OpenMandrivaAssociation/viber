# (tpg) LICENSE ISSUE !!!
# looks like viber license does not say 
# anything whether it allowed or not to 
# redistribute contents of *.deb file in a rpm for or any other
# After some e-mails exchange with Viber support
# answer was strict, and Viber does not allow NOW any kind of redistribution
# Tings may change in future...

Name:			viber
Summary:		Viber Messenger
Version:		4.2
Release:		1
Group:			Networking/Instant messaging
License:		Proprietary
URL:			https://www.viber.com/products/linux
Source0:        http://download.cdn.viber.com/cdn/desktop/Linux/%{name}.deb
BuildRequires:	binutils
BuildRequires:	tar
ExclusiveArch:	x86_64

%description
Viber for Linux lets you send free messages and make free
calls to other Viber users on any device and network,
in any country! Viber syncs your contacts and messages
with your mobile device.

%prep
%setup -cT
cp %{SOURCE0} .
ar x %{name}.deb

%install
mkdir -p %{buildroot}/usr/bin
tar -xvvf data.tar.gz -C %{buildroot}
chmod a+s %{buildroot}/usr/share/viber/Viber
chmod a+s %{buildroot}/usr/share/viber/Viber.sh

%files
%{_datadir}/*
