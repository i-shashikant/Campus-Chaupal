<script>
const store = useCompanyJobsStore();

async function submit() {

    await store.createJob(job);

}
</script>