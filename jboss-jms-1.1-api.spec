%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jms-1.1-api
Version:       1.0.1
Release:       11%{?dist}
Summary:       JBoss JMS API 1.1 Spec
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-jms-api_spec.git jboss-jms-1.1-api
# cd jboss-jms-1.1-api/ && git archive --format=tar --prefix=jboss-jms-1.1-api/ jboss-jms-api_1.1_spec-1.0.1.Final | xz > jboss-jms-1.1-api-1.0.1.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch

%description
The Java Messaging Service 1.1 API classes

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jms-1.1-api
# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README
%license LICENSE

%changelog
* Wed Jul 29 2015 gil cattaneo <puntogil@libero.it> 1.0.1-11
- fix FTBFS rhbz#1239594
- fix BR list and use BRs mvn()-like
- minor changes for adapt to current guideline
- introduce license macro
- resolve some rpmlint problem

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 01 2014 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-9
- New guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed R and BR

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309gitc251f89
- Packaging after license cleanup upstream

* Mon Feb 14 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

