// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Storage
{
    public static class GetProjectServiceAccount
    {
        /// <summary>
        /// Get the email address of a project's unique [automatic Google Cloud Storage service account](https://cloud.google.com/storage/docs/projects#service-accounts).
        /// 
        /// For each Google Cloud project, Google maintains a unique service account which
        /// is used as the identity for various Google Cloud Storage operations, including
        /// operations involving
        /// [customer-managed encryption keys](https://cloud.google.com/storage/docs/encryption/customer-managed-keys)
        /// and those involving
        /// [storage notifications to pub/sub](https://cloud.google.com/storage/docs/gsutil/commands/notification).
        /// This automatic Google service account requires access to the relevant Cloud KMS keys or pub/sub topics, respectively, in order for Cloud Storage to use
        /// these customer-managed resources.
        /// 
        /// The service account has a well-known, documented naming format which is parameterised on the numeric Google project ID.
        /// However, as noted in [the docs](https://cloud.google.com/storage/docs/projects#service-accounts), it is only created when certain relevant actions occur which
        /// presuppose its existence.
        /// These actions include calling a [Cloud Storage API endpoint](https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount/get) to yield the
        /// service account's identity, or performing some operations in the UI which must use the service account's identity, such as attempting to list Cloud KMS keys
        /// on the bucket creation page.
        /// 
        /// Use of this data source calls the relevant API endpoint to obtain the service account's identity and thus ensures it exists prior to any API operations
        /// which demand its existence, such as specifying it in Cloud IAM policy.
        /// Always prefer to use this data source over interpolating the project ID into the well-known format for this service account, as the latter approach may cause
        /// provider update errors in cases where the service account does not yet exist.
        /// 
        /// &gt;  When you write provider code which uses features depending on this service account *and* your provider code adds the service account in IAM policy on other resources,
        ///    you must take care for race conditions between the establishment of the IAM policy and creation of the relevant Cloud Storage resource.
        ///    Cloud Storage APIs will require permissions on resources such as pub/sub topics or Cloud KMS keys to exist *before* the attempt to utilise them in a
        ///    bucket configuration, otherwise the API calls will fail.
        ///    You may need to use `depends_on` to create an explicit dependency between the IAM policy resource and the Cloud Storage resource which depends on it.
        ///    See the examples here and in the `gcp.storage.Notification` resource.
        /// 
        /// For more information see
        /// [the API reference](https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetProjectServiceAccountResult> InvokeAsync(GetProjectServiceAccountArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProjectServiceAccountResult>("gcp:storage/getProjectServiceAccount:getProjectServiceAccount", args ?? new GetProjectServiceAccountArgs(), options.WithVersion());
    }


    public sealed class GetProjectServiceAccountArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The project the unique service account was created for. If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The project the lookup originates from. This field is used if you are making the request
        /// from a different account than the one you are finding the service account for.
        /// </summary>
        [Input("userProject")]
        public string? UserProject { get; set; }

        public GetProjectServiceAccountArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetProjectServiceAccountResult
    {
        /// <summary>
        /// The email address of the service account. This value is often used to refer to the service account
        /// in order to grant IAM permissions.
        /// </summary>
        public readonly string EmailAddress;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Project;
        public readonly string? UserProject;

        [OutputConstructor]
        private GetProjectServiceAccountResult(
            string emailAddress,

            string id,

            string project,

            string? userProject)
        {
            EmailAddress = emailAddress;
            Id = id;
            Project = project;
            UserProject = userProject;
        }
    }
}
