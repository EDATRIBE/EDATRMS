const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout'),
    children: [
      {
        path: '',
        component: () => import('src/layout_pages/Index'),
      },
      {
        path: 'ip/create',
        component: () => import('src/layout_pages/IP/IPCreate'),
      },
      {
        path: 'ann',
        component: () => import('src/layout_pages/Announcement/Announcements')
      },
      {
        path: 'ani',
        component: () => import('src/layout_pages/Animation/Animation')
      },
      {
        path: 'nov',
        component: () => import('src/layout_pages/Novel/Novel')
      },
      {
        path: 'flab',
        component: () => import('pages/flab')
      },
      {
        path: 'con',
        component: () => import('src/layout_pages/Contributor/Contributors')
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
