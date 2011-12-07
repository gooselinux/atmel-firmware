%define usb_version 0.1

Name:           atmel-firmware
Version:        1.3
Release:        7%{?dist}
Summary:        Firmware for Atmel at76c50x wireless network chips

Group:          System Environment/Kernel
License:        Redistributable, no modification permitted
URL:            http://at76c503a.berlios.de/
Source0:        http://www.thekelleys.org.uk/atmel/atmel-firmware-%{version}.tar.gz
Source1:        http://download.berlios.de/at76c503a/at76_usb-firmware-%{usb_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
    
Obsoletes:      at76_usb-firmware < %{usb_version}
Provides:       at76_usb-firmware = %{usb_version}

%description
The drivers for Atmel at76c50x wireless network chips in the Linux 2.6.x kernel 
but do not include the firmware.
This firmware needs to be loaded by the host on most cards using these chips.


%prep
%setup -q 
%setup -q -D -T -a 1 
install -pm 0644 at76_usb-firmware-%{usb_version}/COPYRIGHT COPYRIGHT-usb
install -pm 0644 at76_usb-firmware-%{usb_version}/README README-usb
for i in COPYING README COPYRIGHT-usb README-usb; do
install -pm 0644 ${i} ${i}.%{name}
rm  ${i}
ln -sf /lib/firmware/${i}.%{name} ${i}
done

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/firmware

install -pm 0644 images/*.bin $RPM_BUILD_ROOT/lib/firmware
#install -m 0644 images.usb/* $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 at76_usb-firmware-%{usb_version}/*.bin $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 *.%{name} $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README COPYRIGHT-usb README-usb VERSION
/lib/firmware/*


%changelog
* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 1.3-7
- Add dist tag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 15 2007 kwizart < kwizart at gmail.com > - 1.3-4
- Prevent timestamps changes.

* Thu Dec 13 2007 Ralf Corsépius <rc040203@freenet.de> - 1.3-3
- Don't ship docs in /lib/firmware (BZ 420921).
- Minor spec cleanups.
- Bump %%release to fix F7 -> F8 EVR breakage.

* Mon Aug 27 2007 kwizart < kwizart at gmail.com > - 1.3-2
- Drop the dist tag for firmware

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.3-1
- Initial clean package
