INSERT INTO `django_flatpage` (`id`, `url`, `title`, `content`, `enable_comments`, `template_name`, `registration_required`)
VALUES
	(1,'/public/collect/','Collect','skfdsdf',0,'flatpages/default.html',0),
	(2,'/public/select/','Select','sfg',0,'flatpages/default.html',0),
	(3,'/public/present/','Present','sdf',0,'flatpages/default.html',0),
	(4,'/public/assess/','Assess','dsfsdf',0,'flatpages/default.html',0),
	(5,'/public/about/','Our Philosophy','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in ligula dui, pharetra congue erat. Curabitur vel neque quam. Praesent odio orci, luctus vel rhoncus sit amet, venenatis at arcu. Praesent hendrerit rhoncus ante ac varius. Fusce imperdiet nibh ut diam posuere eget luctus quam tempus. Aliquam erat volutpat. Duis magna mauris, facilisis ac lacinia eget, porttitor id risus. Mauris in est eget mi ornare adipiscing. Ut et enim mi, in pellentesque metus. Aenean eget libero nulla. Quisque dui felis, pharetra sed imperdiet sit amet, commodo ut est. Aliquam congue, magna in suscipit tristique, tortor mauris accumsan velit, et pellentesque massa orci nec erat. Donec eget porta neque. Nunc eget velit nisi, sed dignissim ligula. Donec volutpat arcu in augue porttitor laoreet.\r\n\r\nNulla metus massa, condimentum eu iaculis in, consequat at lectus. Nullam elementum vulputate ante, non vulputate odio scelerisque ac. Vestibulum ut facilisis purus. Vivamus euismod porta fermentum. Sed commodo ultrices ligula vel ultrices. Pellentesque ac magna tortor. Etiam lorem ipsum, ultrices in ultricies at, lobortis nec urna. Aenean vel faucibus tortor. Duis augue nisl, rhoncus faucibus interdum ut, aliquet a justo. Praesent magna augue, placerat at bibendum nec, bibendum facilisis nibh. Nunc euismod molestie nunc, vitae ultrices metus semper sed. Morbi pretium, turpis at dignissim vestibulum, purus velit scelerisque sem, sit amet suscipit massa lacus vel quam. Integer vitae justo a libero placerat scelerisque at ut ligula. Sed non urna quam.\r\n\r\nEtiam auctor neque id nisl porttitor feugiat. Pellentesque purus neque, tempus a porttitor at, tristique eget ligula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Quisque interdum interdum justo eget rhoncus. Suspendisse sit amet tortor sapien, quis tempus mi. Fusce vitae lacus tortor, a pulvinar nulla. Nam ipsum odio, dapibus quis consectetur a, dictum eget nisi. In non enim purus, et consequat libero. Nunc placerat feugiat nulla sed sodales. Maecenas at nisl in turpis faucibus fringilla sollicitudin ut ante. Pellentesque lacinia tellus in purus aliquam a iaculis nisi interdum.\r\n\r\nNam euismod placerat lorem sed rhoncus. Morbi egestas, diam eu porta cursus, arcu urna commodo nisi, sit amet fermentum quam lorem a',0,'flatpages/default.html',0),
	(6,'/','Home','<p>Landing Page</p>\r\n\r\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet nisl magna. Phasellus lobortis ultricies lorem sed pharetra. Etiam mattis pretium eros, sit amet tempus neque faucibus ut. Nam aliquet nisi nec erat consequat id auctor nibh sollicitudin. Quisque quis tempor sem. Aenean facilisis ligula nec lacus volutpat at aliquam felis facilisis. Nulla facilisi. Donec sapien erat, laoreet sit amet auctor id, mattis quis sapien. Mauris in molestie dolor. Nam diam lacus, euismod eu venenatis sed, ornare in arcu. Aliquam fermentum ligula a urna pharetra volutpat. Curabitur urna tellus, malesuada et ullamcorper vitae, venenatis sed erat. Curabitur rutrum, justo eget imperdiet pharetra, erat urna tempor lorem, sed porttitor metus nibh ut eros. Praesent faucibus, tellus sit amet vehicula pretium, sapien lectus fringilla od</p>',0,'flatpages/front.html',0),
	(7,'/public/faq/','FAQs','FAQs goe on this page',0,'',0),
	(8,'/public/contact/','Contact','Contact form',0,'',0);

INSERT INTO `django_flatpage_sites` (`id`, `flatpage_id`, `site_id`)
VALUES
	(4,1,2),
	(8,2,2),
	(7,3,2),
	(3,4,2),
	(2,5,2),
	(1,6,2),
	(6,7,2),
	(5,8,2);