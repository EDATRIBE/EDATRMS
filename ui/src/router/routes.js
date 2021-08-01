const routes = [
    {
        path: '/',
        component: () => import('layouts/MainLayout'),
        children: [
            {
                path: '',
                redirect: 'index'
            },
            {
                path: 'index',
                component: () => import('src/layout_pages/Index/Index'),
                children: [
                    {
                        path: '',
                        redirect: 'animations'
                    },
                    {
                        path: 'animations',
                        component: () => import('src/layout_pages/Index/IndexAnimations'),
                    },
                    {
                        path: 'novels',
                        component: () => import('src/layout_pages/Index/IndexNovels'),
                    },
                    {
                        path: 'ips_and_tags',
                        component: () => import('src/layout_pages/Index/IndexIPsAndTags'),
                    }
                ]
            },
            {
                path: 'ip',
                component: () => import('src/layout_pages/IP/IPLayout'),
                children: [
                    {
                        path: 'create',
                        component: () => import('src/layout_pages/IP/IPCreate')
                    },
                    {
                        path: 'edit',
                        component: () => import('src/layout_pages/IP/IPEdit')
                    }
                ]
            },
            {
                path: 'ann',
                component: () => import('src/layout_pages/Announcement/Announcements')
            },
            {
                path: 'animation',
                component: () => import('src/layout_pages/Animation/AnimationLayout'),
                children: [
                    {
                        path: 'info',
                        component: () => import('src/layout_pages/Animation/AnimationInfo')
                    },
                    {
                        path: 'create',
                        component: () => import('src/layout_pages/Animation/AnimationCreate')
                    },
                    {
                        path: 'edit',
                        component: () => import('src/layout_pages/Animation/AnimationEdit')
                    },
                    {
                        path: 'caption',
                        component: () => import('src/layout_pages/Animation/Caption/CaptionLayout'),
                        children: [
                            {
                                path: 'create',
                                component:() => import('src/layout_pages/Animation/Caption/CaptionCreate')
                            }
                        ]
                    },
                    {
                        path: 'video',
                        component: () => import('src/layout_pages/Animation/Video/VideoLayout'),
                        children: [
                            {
                                path: 'create',
                                component:() => import('src/layout_pages/Animation/Video/VideoCreate')
                            }
                        ]
                    }
                ]
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
