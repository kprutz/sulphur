import React from 'react'
import { useTranslation } from 'react-i18next'

import 'App.css'
import { SensorsContainer } from 'features/sensors'
import TitleTypography from 'libs/ui/components/TitleTypography'

const HomePage = () => {
  const { t } = useTranslation()

  return (
    <>
       <SensorsContainer />
    </>
  )
}

export default HomePage
