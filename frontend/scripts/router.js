import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from './pages/index'
import Project from './pages/project'
import NewProject from './pages/new_project'
import ProjectSettings from './pages/project_settings'
import ProjectReports from './pages/project_reports'
import ProjectReport from './pages/project_report'
import ProjectHome from './pages/project_home'
import EstimatePeople from './pages/estimate_people'
import EstimateTransports from './pages/estimate_transports'
import EstimateExtras from './pages/estimate_extras'
import EstimateLocations from './pages/estimate_locations'


Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/project/:project_id',
      component: Project,
      children: [
        {
          path: '',
          name: 'project_home',
          component: ProjectHome
        },
        {
          path: 'settings',
          name: 'project_settings',
          component: ProjectSettings
        },

        {
          path: 'persons',
          name: 'estimate_people',
          component: EstimatePeople
        },
        {
          path: 'transports',
          name: 'estimate_transports',
          component: EstimateTransports
        },
        {
          path: 'extras',
          name: 'estimate_extras',
          component: EstimateExtras
        },
        {
          path: 'locations',
          name: 'estimate_locations',
          component: EstimateLocations
        },
        {
          path: 'reports',
          name: 'project_reports',
          component: ProjectReports
        },
        {
          path: 'report/:report_id',
          name: 'project_report',
          component: ProjectReport
        }
      ]
    },
    {
      path: '/new',
      name: 'new',
      component: NewProject
    }
  ]
})