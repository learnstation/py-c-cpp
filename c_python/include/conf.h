#ifndef CONF_H_
#define CONF_H_

#ifdef _WIN32

#ifdef SHARE_EXE
#ifdef DLLEXPORT	/* { */
#define D_API __declspec(dllexport)
#else				/* }{ */
#define D_API __declspec(dllimport)
#endif

#else
#define D_API
#endif

#else
#define D_API
#endif

#endif